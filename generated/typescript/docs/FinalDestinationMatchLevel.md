
# FinalDestinationMatchLevel

Match level describing the geographical level to which an address has been matched.  It can be one of the following:    - Unit   - StreetNumber   - Street   - Postalcode  See: http://localhost:4321/reference/search-confidence/ 

## Properties

Name | Type
------------ | -------------

## Example

```typescript
import type { FinalDestinationMatchLevel } from '@naurt/api'

// TODO: Update the object below with actual values
const example = {
} satisfies FinalDestinationMatchLevel

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as FinalDestinationMatchLevel
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


