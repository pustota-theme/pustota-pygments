# pustota-pygments

[![test](https://github.com/pustota-theme/pustota-pygments/actions/workflows/test.yml/badge.svg?event=push)](https://github.com/pustota-theme/pustota-pygments/actions/workflows/test.yml)
[![codecov](https://codecov.io/gh/pustota-theme/pustota-pygments/branch/master/graph/badge.svg)](https://codecov.io/gh/pustota-theme/pustota-pygments)
[![Python Version](https://img.shields.io/pypi/pyversions/pustota-pygments.svg)](https://pypi.org/project/pustota-pygments/)
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)

pustota theme for pygments for code highlighting.


## Features

- Highlights you core with [`pygmentize`](https://pygments.org)
- Follows [`pustota` theme](https://github.com/pustota-theme/pustota) colors


## Usage

We recommend using [`uvx`](https://docs.astral.sh/uv/guides/tools/).

Dark theme:

![pustota](https://raw.githubusercontent.com/pustota-theme/pustota-pygments/master/assets/dark.png)

```bash
uvx --with pustota-pygments pygemntize \
  -f rtf -P style=pustota -O fontface='Menlo' \
  $FILENAME | pbcopy
```

Light theme:

![pustota](https://raw.githubusercontent.com/pustota-theme/pustota-pygments/master/assets/light.png)

```bash
uvx --with pustota-pygments pygemntize \
  -f rtf -P style=pustota-light -O fontface='Menlo' \
  $FILENAME | pbcopy
```

Instead of `pbcopy` you might need another copy tool for your OS.


## License

[MIT](https://github.com/pustota-theme/pustota-pygments/blob/master/LICENSE)

## Credits

This project was generated with [`wemake-python-package`](https://github.com/wemake-services/wemake-python-package). Current template version is: [e00027b714460fb8b35cdd98a3705af58475c3e2](https://github.com/wemake-services/wemake-python-package/tree/e00027b714460fb8b35cdd98a3705af58475c3e2). See what is [updated](https://github.com/wemake-services/wemake-python-package/compare/e00027b714460fb8b35cdd98a3705af58475c3e2...master) since then.
