Bundle into a single file with

```
redocly bundle src/naurt.yaml -o output.yaml
```

Compile that into a library

## Rust

```
openapi-generator generate -i output.yaml -g rust -o generated/rust -t templates/rust --additional-properties=packageName=naurt-api
```

Then change directory to `generated/rust` and run `cargo publish`. You may first 
need to `cargo login` to use your crates.io API key

## Python

For python, we use the `openapi-python-client` found [here](https://github.com/openapi-generators/openapi-python-client)

It can be installed from the [AUR](https://aur.archlinux.org/packages/openapi-python-client)

```
yay -S openapi-python-client
```

In `config/python.yaml` before each release you'll need to bump the package 
version number.

The package can be generated via

```
openapi-python-client generate --path output.yaml --config config/python.yaml --output-path generated/python --overwrite --custom-template-path templates/python
```

For uploading, you'll need to installed [twine](https://archlinux.org/packages/extra/any/twine/)

```
pacman -S twine
```

I suggest you try using the [TestPyPi](https://test.pypi.org/) first. Sign up,
and add an API key. To your `.pypirc` add

```
[testpypi]
  username = __token__
  password = <SUPER-SECRET-API-KEY-HERE>
```

From `generated/python` build with 

```
python -m build
```

(you may need to run `python -m pip install --upgrade build`)

Upload to TestPyPi with 

```
twine upload --repository testpypi dist/*
```

And you can then install with 

```
python -m pip install -i https://test.pypi.org/simple/ naurt-api==0.1.0
```

Or the relevant version number.

Assuming that works as expected, we can push to the main PyPi repo. The steps 
are similar. Now `.pypirc` should also contain

```
[pypi]
  username = __token__
  password = <SUPER-SECRET-API-KEY-HERE>
```

And finally

```
twine upload --repository pypi dist/*
```

## Go

```
openapi-generator generate -i output.yaml -g go -o generated/go -c config/go.yaml
```

## TypeScript

```
openapi-generator generate -i output.yaml -g typescript-fetch -o generated/typescript -c config/typescript.yaml -t templates/typescript
```