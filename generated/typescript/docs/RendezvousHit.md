
# RendezvousHit


## Properties

Name | Type
------------ | -------------
`centre` | [RendezvousHitData](RendezvousHitData.md)
`covers` | [Array&lt;RendezvousHitData&gt;](RendezvousHitData.md)

## Example

```typescript
import type { RendezvousHit } from '@naurt/api'

// TODO: Update the object below with actual values
const example = {
  "centre": null,
  "covers": null,
} satisfies RendezvousHit

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as RendezvousHit
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


