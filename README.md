# Basic Calkit example

This is a basic Calkit example project,
which includes data collection,
figure and table generation,
and LaTeX article compilation,
all part of a single reproducible pipeline.
The article pulls its figure, table, and numbers straight from the
pipeline's outputs with the `calkit` LaTeX package,
and builds in a TeX Live environment Calkit installs,
so Docker isn't needed.

You can also view this project on
[calkit.io](https://calkit.io/calkit/example-basic).

This project can be reproduced with:

```sh
calkit run
```

## How to use this project as a template

With the Calkit CLI:

```sh
calkit new project --template calkit/example-basic
```

or click "use this project as a template" at https://calkit.io/calkit/example-basic:

<img width="1068" height="667" alt="Image" src="https://github.com/user-attachments/assets/8ead705e-b92f-4e66-a346-22e238012da6" />
