import pytest

def test_html_exists():
    # Ellenőrizzük, hogy az index.html fájl létezik-e
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
        assert content, "Az index.html fájl üres!"

def test_css_exists():
    # Ellenőrizzük, hogy a style.css fájl létezik-e
    with open('styles.css', 'r', encoding='utf-8') as f:
        content = f.read()
        assert content, "A style.css fájl üres!"

def test_html_structure():
    # Ellenőrizzük, hogy a HTML fájl tartalmazza-e a container div-et
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
        assert '<div class="container">' in content, "A container div nem található a HTML-ben!"
        assert '<h1>' in content, "A h1 elem nem található a HTML-ben!"

def test_css_structure():
    # Ellenőrizzük, hogy a CSS fájl tartalmazza-e a h1 és container stílusokat
    with open('styles.css', 'r', encoding='utf-8') as f:
        content = f.read()
        assert 'h1 {' in content, "A h1 stílus nem található a CSS fájlban!"
        assert '.container {' in content, "A container stílus nem található a CSS fájlban!"
