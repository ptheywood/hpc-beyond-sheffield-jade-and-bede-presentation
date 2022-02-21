# HPC Beyond Sheffield: JADE and Bede Presentation

> Alongside the local HPC facilities at The University of Sheffield, researchers can also access regional Tier-2 HPC facilities in the UK.
>
> This talk will describe the Tier-2 HPC systems available to TUoS researchers, why using Tier-2 HPC can be beneficial and how these systems can be accessed and used.
>
> There will be a focus on the JADE and Bede GPU-based Tier 2 systems which TUoS is affiliated with.


---

This is a reveal.js presentation, written in markdown using [webpro/reveal-md](https://github.com/webpro/reveal-md)

It was originally presented as part of the [RSE Sheffield LunchBytes series on 2022-02-17](https://rse.shef.ac.uk/events/lunchbytes-2022-02-17.html).

[![CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)][cc-by]

## Building the presentation

<!-- ### Docker / Singularity

> @todo - building in docker / singularity. -->

### Local nvm installation

1. Install `nvm` as described at [nvm-sh/nvm](https://github.com/nvm-sh/nvm#installing-and-updating)
2. Install node via nvm

    ```bash
    nvm install --lts
    ```

3. Install `reveal-md` via `npm`

    ```bash
    npm install -g reveal-md
    ```

### Building the slides

```bash
reveal-md slides.md --static _static --static-dirs=assets
```

### Running a web server

```bash
reveal-md slides.md -w
```

### Using chrome in app mode

```
google-chrome --app="http://localhost:1948/slides.md"
```

### Speaker view

Press `s` to open speaker view when running via a server

## Licence

Slide contents are licensed under a
[Creative Commons Attribution 4.0 International License][cc-by].

Logos and images in `assets/img/logos` and `/assets/img/thirdparty` are copyright their respective owners.

[![CC BY 4.0](https://i.creativecommons.org/l/by/4.0/88x31.png)][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/
