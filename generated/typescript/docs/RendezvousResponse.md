
# RendezvousResponse


## Properties

Name | Type
------------ | -------------
`responses` | [Array&lt;RendezvousHit&gt;](RendezvousHit.md)
`unmatched` | [Array&lt;RendezvousQuery&gt;](RendezvousQuery.md)
`version` | string
`requestId` | string

## Example

```typescript
import type { RendezvousResponse } from '@naurt/api'

// TODO: Update the object below with actual values
const example = {
  "responses": null,
  "unmatched": null,
  "version": null,
  "requestId": null,
} satisfies RendezvousResponse

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as RendezvousResponse
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


