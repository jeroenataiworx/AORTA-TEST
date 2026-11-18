#!/usr/bin/env python3
"""ResearchMaster GitHub Static Export 0.1.0: publish MkDocs 1.0.6 output without changing sources."""
import argparse
import datetime as dt
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import zipfile

VERSION = '0.1.3'
SKIP = {'.DS_Store', 'Thumbs.db'}

def copy_tree(src, dst):
    for p in src.rglob('*'):
        if p.is_symlink():
            raise ValueError(f'Symbolische link niet toegestaan: {p}')
        if any(x in SKIP or x == '__MACOSX' for x in p.relative_to(src).parts):
            continue
        q = dst / p.relative_to(src)
        if p.is_dir(): q.mkdir(parents=True, exist_ok=True)
        elif p.is_file():
            q.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(p, q)

def locate(root):
    if (root / 'catalog.ttl').is_file(): return root
    matches = [p for p in root.iterdir() if p.is_dir() and (p / 'catalog.ttl').is_file()]
    if len(matches) == 1: return matches[0]
    raise ValueError('Bronpackage niet eenduidig gevonden (catalog.ttl).')

def unpack(src, dest):
    if src.is_dir():
        copy_tree(src, dest)
    elif zipfile.is_zipfile(src):
        with zipfile.ZipFile(src) as z:
            for info in z.infolist():
                path = Path(info.filename)
                if path.is_absolute() or '..' in path.parts:
                    raise ValueError(f'Onveilig ZIP-pad: {info.filename}')
                if info.is_dir() or any(x in SKIP or x == '__MACOSX' for x in path.parts): continue
                target = dest.joinpath(*path.parts)
                target.parent.mkdir(parents=True, exist_ok=True)
                with z.open(info) as f, target.open('wb') as g: shutil.copyfileobj(f,g)
    else: raise ValueError('Bronpackage moet directory of ZIP zijn.')
    return locate(dest)

def sha256(path):
    h = hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda:f.read(1024*1024), b''): h.update(block)
    return h.hexdigest()

def zip_dir(root, zip_path):
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED, compresslevel=6) as z:
        for p in sorted(root.rglob('*')):
            if p.is_file(): z.write(p, p.relative_to(root).as_posix())

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('bronpackage', type=Path, nargs='?', default=None,
                        help='Optioneel: AORTA Harvester-map of ZIP (standaard ../aorta_8_5_2)')
    parser.add_argument('--mkdocs-project', type=Path, default=None,
                        help='Optioneel: MkDocs-project (standaard ./aorta_8_5_2_mkdocs)')
    parser.add_argument('--output', type=Path, default=None,
                        help='Optioneel: uitvoermap (standaard ./github_export)')
    parser.add_argument('--repo', default='AORTA-TEST', help='Naam GitHub repository en Pages basispad')
    parser.add_argument('--owner', default='jeroenataiworx', help='GitHub gebruikersnaam of organisatie')
    parser.add_argument('--replace', action='store_true')
    args = parser.parse_args()
    # Standaardlocaties zijn relatief aan de mkdoc-map, ongeacht de werkdirectory.
    script_dir = Path(__file__).resolve().parent
    mkdoc_root = script_dir if script_dir.name == 'mkdoc' else Path.cwd().resolve()
    source = (args.bronpackage or (mkdoc_root.parent / 'aorta_8_5_2')).resolve()
    project = (args.mkdocs_project or (mkdoc_root / 'aorta_8_5_2_mkdocs')).resolve()
    output = (args.output or (mkdoc_root / 'github_export')).resolve()
    if not source.exists():
        alternatives = sorted(mkdoc_root.parent.glob('aorta_8_5_2*.zip'))
        if len(alternatives) == 1:
            source = alternatives[0].resolve()
        else:
            parser.error(f'Bronpackage ontbreekt: {source}; geef het pad expliciet op.')
    if not (project / 'mkdocs.yml').is_file(): parser.error('MkDocs-project mist mkdocs.yml')
    if not (project / 'docs').is_dir(): parser.error('MkDocs-project mist docs/')
    if not shutil.which('mkdocs'): parser.error('mkdocs ontbreekt: pip install mkdocs-material')
    if not args.repo or '/' in args.repo or '\\' in args.repo or args.repo in ('.', '..'):
        parser.error('Ongeldige repositorynaam')
    dest = output / args.repo
    zip_path = output / (args.repo + '_GitHub_Static_Export_' + VERSION + '.zip')
    if dest.exists() and not args.replace: parser.error(f'Bestaat al: {dest}; gebruik --replace')
    if zip_path.exists() and not args.replace: parser.error(f'Bestaat al: {zip_path}; gebruik --replace')
    if any(p == source or p in source.parents or p == project or p in project.parents for p in [dest, output]):
        parser.error('Uitvoer mag niet binnen de bronpackage of het MkDocs-project liggen')
    output.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='.rm_github_stage_', dir=output) as td:
        stage = Path(td) / args.repo
        stage.mkdir()
        src_root = unpack(source, Path(td) / 'input')
        source_out = stage / 'source'
        source_out.mkdir()
        # Retain the complete Harvester package including any supplementary RDF, HTML and issues.
        copy_tree(src_root, source_out)
        # Build from a copy of the exact MkDocs project, not a rewritten or parallel renderer.
        mkcopy = Path(td) / 'mkdocs_project'
        copy_tree(project, mkcopy)
        shutil.rmtree(mkcopy / 'site', ignore_errors=True)
        # Alleen de tijdelijke MkDocs-config aanpassen. De lokale baseline blijft intact.
        try:
            import yaml
        except ImportError as exc:
            raise ValueError('PyYAML ontbreekt; installeer mkdocs-material') from exc
        config_path = mkcopy / 'mkdocs.yml'
        config = yaml.safe_load(config_path.read_text(encoding='utf-8'))
        config['site_url'] = f'https://{args.owner}.github.io/{args.repo}/'
        config_path.write_text(yaml.safe_dump(config, allow_unicode=True, sort_keys=False), encoding='utf-8')
        subprocess.run(['mkdocs', 'build', '--config-file', str(mkcopy / 'mkdocs.yml'), '--site-dir', str(stage / 'docs')], check=True)
        site = stage / 'docs'
        if not (site / 'index.html').is_file(): raise ValueError('Build heeft geen docs/index.html opgeleverd')
        search = list(site.rglob('search_index.json'))
        if not search: raise ValueError('Zoekindex ontbreekt; export geweigerd')
        # GitHub Pages: static files served from /docs on main branch.
        (site / '.nojekyll').write_text('', encoding='utf-8')
        (stage / 'README.md').write_text(
            '# AORTA-documentatie – GitHub-export\n\n'
            'Deze repository bevat twee representaties van dezelfde bronpackage:\n\n'
            '- **[Website](docs/index.html)**: de statische MkDocs-website; op GitHub Pages via de Pages-URL.\n'
            '- **[Bronpackage](source/)**: oorspronkelijke bestanden, inclusief Markdown, TTL, assets en manifest.\n\n'
            'De website is gebouwd uit het bestaande ResearchMaster MkDocs 1.0.6-project. '
            'De bestanden in `source/` zijn inhoudelijk ongewijzigd.\n\n'
            'Zie **[GITHUB_INSTELLEN.md](GITHUB_INSTELLEN.md)** voor het uploaden en publiceren.\n', encoding='utf-8')
        # Instructie is optioneel naast het script; bij ontbreken wordt deze gegenereerd.
        guide_path = Path(__file__).with_name('GITHUB_INSTELLEN.md')
        if False and guide_path.is_file():
            guide = guide_path.read_text(encoding='utf-8')
        else:
            guide = (
                '# GitHub instellen\n\n'
                '1. Maak een GitHub-repository aan.\n'
                '2. Upload de volledige inhoud van deze exportmap naar de hoofdbranch.\n'
                '3. Ga naar Settings > Pages en kies Deploy from a branch, '
                'branch main, folder /docs.\n'
                '4. Open de Pages-URL zodra GitHub de publicatie heeft voltooid.\n\n'
                'Let op: een private repository maakt GitHub Pages niet automatisch besloten.\n'
            )
        (stage / 'GITHUB_INSTELLEN.md').write_text(guide, encoding='utf-8')
        files = sorted(p for p in source_out.rglob('*') if p.is_file())
        index = {
            'generator': 'ResearchMaster GitHub Static Export', 'version': VERSION,
            'mkdocsBaseline': '1.0.6', 'generatedAtUtc': dt.datetime.now(dt.timezone.utc).isoformat(),
            'sourcePackageName': src_root.name,
            'sourceFiles': [{'path':p.relative_to(source_out).as_posix(), 'sha256':sha256(p)} for p in files],
            'websiteRoot': 'docs/', 'searchIndexPaths': [p.relative_to(stage).as_posix() for p in search],
            'sourceRoot': 'source/'
        }
        (stage / 'PUBLICATIE_MANIFEST.json').write_text(json.dumps(index, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
        # Protect against accidentally shipping git history, secrets and editor caches.
        (stage / '.gitignore').write_text('.DS_Store\n__pycache__/\n*.pyc\n', encoding='utf-8')
        if dest.exists():
            # Behoud de bestaande .git-repository, zodat volgende pushes gewoon werken.
            for item in dest.iterdir():
                if item.name == '.git':
                    continue
                if item.is_dir(): shutil.rmtree(item)
                else: item.unlink()
            for item in stage.iterdir():
                shutil.move(str(item), str(dest / item.name))
        else:
            shutil.move(str(stage), str(dest))
    if zip_path.exists(): zip_path.unlink()
    zip_dir(dest, zip_path)
    print(f'Uploadmap: {dest}\nZIP: {zip_path}\nBronbestanden: {len(files)}\nZoekindex: {len(search)}')

if __name__ == '__main__':
    try: main()
    except (ValueError, OSError, subprocess.CalledProcessError) as e:
        print(f'FOUT: {e}', file=sys.stderr)
        sys.exit(1)
