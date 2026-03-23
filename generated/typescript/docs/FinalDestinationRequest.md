
# FinalDestinationRequest

A single request to the API, which can contain up to 200 queries. Each query  is independent and can be of a different type. 

## Properties

Name | Type
------------ | -------------
`queries` | [Array&lt;FinalDestinationQuery&gt;](FinalDestinationQuery.md)
`options` | [FinalDestinationOptions](FinalDestinationOptions.md)

## Example

```typescript
import type { FinalDestinationRequest } from '@naurt/api'

// TODO: Update the object below with actual values
const example = {
  "queries": null,
  "options": null,
} satisfies FinalDestinationRequest

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as FinalDestinationRequest
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


