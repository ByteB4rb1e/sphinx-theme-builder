# Sphinx Theme Builder

<!-- start-elevator-pitch -->

Streamline the Sphinx theme development workflow, by building upon existing
standardised tools.

- simplified packaging experience
- simplified JavaScript tooling setup
- development server, with rebuild-on-save and automagical browser reloading
- consistent repository structure across themes

<!-- end-elevator-pitch -->

> This is a fork of `pradyunsg/sphinx-theme-builder`, specifically for allowing the
> circumvention of Node.js environment bootstrapping through `nodeenv`. The
> workflow is identitical, except for defaulting to using the system's Node.js
> installation, which can be overridden by setting the `STB_USE_SYSTEM_NODE`
> environment variable to `0` or `False`.
> 
> The minum system requirements for the system's Node.js environment are
> *v18.19.1* for `node`, and *v9.9.3* for `npm`.

## Installation

<!-- start-installation -->

To use this fork in a project with an existing theme using
`pradyunsg/sphinx-theme-builder`, edit the `requires` field within the
`[build-system]` section in the `pyproject.toml` of the theme:

```
[build-system]
requires = ["sphinx-theme-builder @ git+https://github.com/ByteB4rb1e/sphinx-theme-builder.git@main"]
build-backend = "sphinx_theme_builder"
```

This project requires modern versions of CPython (>= 3.10).

<!-- end-installation -->

## Usage

Find more details on how to use this project in the [documentation].

## Contributing

`stb` is a volunteer maintained open source project, and we welcome
contributions of all forms. Please take a look at the [Development
Documentation] for more information.

[documentation]: https://sphinx-theme-builder.rtfd.io/
[development documentation]:
  https://sphinx-theme-builder.rtfd.io/en/latest/development/
