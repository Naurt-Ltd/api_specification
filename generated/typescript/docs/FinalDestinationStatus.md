
# FinalDestinationStatus

The `queries` and `responses` arrays are always 1:1. If no match can be found, a 404 will NOT be returned. Instead, check this enum for `no_matches`. That  indicates no error has happened, but nothing was found. `ok` when something is found. 

## Properties

Name | Type
------------ | -------------

## Example

```typescript
import type { FinalDestinationStatus } from '@naurt/api'

// TODO: Update the object below with actual values
const example = {
} satisfies FinalDestinationStatus

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as FinalDestinationStatus
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


