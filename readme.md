# HPC Beyond Sheffield: JADE and Bede Presentation

> Alongside the local HPC facilities at The University of Sheffield, researchers can also access regional Tier-2 HPC facilities in the UK.
> This talk will describe the Tier-2 HPC systems available to TUoS researchers, why using Tier-2 HPC can be beneficial and how these systems can be accessed and used.
> There will be a focus on the JADE and Bede GPU-based Tier 2 systems which TUoS is affiliated with.

This is a reveal.js presentation, written in markdown.

It was originally presented as part of the [RSE Sheffield LunchBytes series on 2022-02-17](https://rse.shef.ac.uk/events/lunchbytes-2022-02-17.html).

## Building the presentation

### Docker / Singularity

> @todo - building in docker / singularity.

### Using VS Code plugin

VS Code has several plugins for creating markdown-based revealjs presentations, such as [tokiedokie.reveal-markdown](https://marketplace.visualstudio.com/items?itemName=tokiedokie.reveal-markdown).

+ `Ctrl + p`
+ `ext install tokiedokie.reveal-markdown`

The slides can then be previewed whilst writing them via:

+ `Ctrl + Shift + p`
+ `Revealjs: Show presentation by side`

Opened in a browser:

+ `Ctrl + Shift + p`
+ `Revealjs: Open presentation in a browser`

Exported to HTML

+ `Ctrl + Shift + p`
+ `Revealjs: Export in HTML`

Exported to PDF

+ `Ctrl + Shift + p`
+ `Revealjs: Export in PDF`

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

```bash
reveal-md slides.md --static _static --static-dirs=assets
```

```bash
reveal-md slides.md -w
# Open in chrome without toolbars
google-chrome --app="http://localhost:1948/slides.md"
```

Press S to open speaker view when running via the server.
