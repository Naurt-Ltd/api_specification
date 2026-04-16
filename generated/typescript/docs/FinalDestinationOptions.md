
# FinalDestinationOptions

`options` impact all `queries` within a request 

## Properties

Name | Type
------------ | -------------
`prettyPrint` | boolean
`verbose` | boolean
`structuredResponse` | boolean
`geojsonType` | [GeojsonType](GeojsonType.md)
`returnOriginal` | boolean
`inputFilter` | [InputFilter](InputFilter.md)
`sourceId` | [SourceIdRequest](SourceIdRequest.md)

## Example

```typescript
import type { FinalDestinationOptions } from '@naurt/api'

// TODO: Update the object below with actual values
const example = {
  "prettyPrint": null,
  "verbose": null,
  "structuredResponse": null,
  "geojsonType": null,
  "returnOriginal": null,
  "inputFilter": null,
  "sourceId": null,
} satisfies FinalDestinationOptions

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as FinalDestinationOptions
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


