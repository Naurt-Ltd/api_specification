
# SourceIdRequest

Use this to request that Naurt returns a source ID for the addresses. Note that  if a requested source ID is not available for that address, this option will  be ignored. 

## Properties

Name | Type
------------ | -------------
`osUprn` | boolean
`osUdprn` | boolean

## Example

```typescript
import type { SourceIdRequest } from '@naurt/api'

// TODO: Update the object below with actual values
const example = {
  "osUprn": null,
  "osUdprn": null,
} satisfies SourceIdRequest

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as SourceIdRequest
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


