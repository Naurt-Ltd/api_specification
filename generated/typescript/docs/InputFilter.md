
# InputFilter

Input filtering helps when you have addresses from sources you can\'t control. Sometimes, providers might miss out on important parts of addresses, like a street number or postcode. If Naurt detects that an address is missing too  many fields to be likely to give a good match, it can be rejected by this  feature  `none` turns this feature off and does not do any input filtering. This may  result in some poor responses  `loose` is the default - it does filter out some poor inputs but allows some  missing fields   `strict` is our strictest, and only allows searches which are likely to produce good matches 

## Properties

Name | Type
------------ | -------------

## Example

```typescript
import type { InputFilter } from '@naurt/api'

// TODO: Update the object below with actual values
const example = {
} satisfies InputFilter

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as InputFilter
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


