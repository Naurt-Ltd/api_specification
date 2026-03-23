
# FeatureProperties


## Properties

Name | Type
------------ | -------------
`naurtType` | string
`accuracy` | [Accuracy](Accuracy.md)
`minimumParkingToDoorDistance` | number

## Example

```typescript
import type { FeatureProperties } from '@naurt/api'

// TODO: Update the object below with actual values
const example = {
  "naurtType": null,
  "accuracy": null,
  "minimumParkingToDoorDistance": null,
} satisfies FeatureProperties

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as FeatureProperties
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


