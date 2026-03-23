
# FinalDestinationLogging


## Properties

Name | Type
------------ | -------------
`info` | Array&lt;string&gt;
`warnings` | Array&lt;string&gt;
`errors` | Array&lt;string&gt;

## Example

```typescript
import type { FinalDestinationLogging } from '@naurt/api'

// TODO: Update the object below with actual values
const example = {
  "info": null,
  "warnings": null,
  "errors": null,
} satisfies FinalDestinationLogging

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as FinalDestinationLogging
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


