
# RendezvousHitData


## Properties

Name | Type
------------ | -------------
`id` | string
`address` | string
`geojson` | [FeatureCollection](FeatureCollection.md)
`distance` | number

## Example

```typescript
import type { RendezvousHitData } from '@naurt/api'

// TODO: Update the object below with actual values
const example = {
  "id": null,
  "address": null,
  "geojson": null,
  "distance": null,
} satisfies RendezvousHitData

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as RendezvousHitData
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


