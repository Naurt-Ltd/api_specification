
# FinalDestinationHits


## Properties

Name | Type
------------ | -------------
`bestMatch` | [FinalDestinationHit](FinalDestinationHit.md)
`additionalMatches` | [Array&lt;FinalDestinationHit&gt;](FinalDestinationHit.md)
`status` | [FinalDestinationStatus](FinalDestinationStatus.md)
`originalRequest` | [FinalDestinationQuery](FinalDestinationQuery.md)

## Example

```typescript
import type { FinalDestinationHits } from '@naurt/api'

// TODO: Update the object below with actual values
const example = {
  "bestMatch": null,
  "additionalMatches": null,
  "status": null,
  "originalRequest": null,
} satisfies FinalDestinationHits

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as FinalDestinationHits
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


