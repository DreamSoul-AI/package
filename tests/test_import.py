from importlib.resources import files


def test_import():
    import package
    pkg_root = files("package")

    readme = (pkg_root / "README.md").read_text(encoding="utf-8")
    license = (pkg_root / "LICENSE").read_text(encoding="utf-8")

    print(readme)
    print(license)
    return


def main():
    test_import()


if __name__ == "__main__":
    main()



