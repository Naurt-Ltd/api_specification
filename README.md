Bundle into a single file with

```
redocly bundle src/naurt.yaml -o output.yaml
```

Compile that into a library

```
openapi-generator generate -i output.yaml -g rust -o generated/rust
```