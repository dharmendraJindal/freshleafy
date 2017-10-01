# md-colors

> Material Design's colors as SASS variables, extensions, or functions

[![npm package][npm-ver-link]][releases]
[![][dl-badge]][npm-pkg-link]

## Install

```a
npm install md-colors
# or
bower install md-colors
```

## Usage

```sass
@import 'md-colors'

// declare variables
$primary   : md-color('blue', '300')
$secondary : md-color('red', 'a300')

// via Function
.eg--function
	color: md-color('deep-purple', '50')
	background-color: md-color('indigo') // '500' is default shade
	box-shadow: 0 1px 3px rgba(md-color('lime'), 0.2)

// via Extension
.eg--placeholder
	@extend %md-color-deep-purple-50
	@extend %md-bg-color-indigo-500
	// No built-in extension for 'box-shadow'. Use a function
```

### Colors

All of `md-color`'s colors are taken from the [Material Design Color Palette](https://www.google.com/design/spec/style/color.html#color-color-palette).

All names and values are stringified (within functions) and lowercased. For example:

```sass
// function
color: md-color('light-blue', 'a100')
background-color: md-color('green', '600')

// extension/placeholder
@extend %md-color-lime-a200
@extend %md-bg-color-red-300
```

### Importing

You have two options for easy importing:

* Attach `node_modules` or `bower_components` to the `includePaths` option of your SASS compiler
* Use a sass `importer` function, as [described here](http://stackoverflow.com/a/29924381) or as [exemplified here](https://www.npmjs.com/package/sass-module-importer)

### Function

SASS functions can be anywhere as if they were normal variables or values.

The `md-color` function takes two parameters:

#### name

Type: `string`

The lowercased (and hypened) color name; eg: `red`, `light-purple`

#### shade

Type: `string`
Default: `500`

The shade or weight of the color; eg: `50`, `300`, `a100`

### Extensions

By nature, extensions, or "placeholders", don't offer too much without inordinate amounts of complexity. So there are only two sets of built-in extensions for `background`s and `color`s.

If you want a text-color extension, the format is:

```sass
%md-color-{ name }-{ shade }
```

If you want a background color extension, the format is:

```sass
%md-bg-color-{ name }-{ shade }
```

For example:

```sass
body
	@extend %md-color-deep-purple-50
	@extend %md-bg-color-indigo-500

.test
	position: relative
	@extend %md-color-deep-purple-50
	@extend %md-bg-color-indigo-500
```

Output:

```css
body,
.test {
	color: #EDE7F6; }
body,
.test {
	background-color: #3F51B5; }
.test {
	position: relative; }
```

## License

MIT © [Luke Edwards](https://lukeed.com)

[releases]:     https://github.com/lukeed/md-colors/releases
[npm-pkg-link]: https://www.npmjs.org/package/md-colors
[npm-ver-link]: https://img.shields.io/npm/v/md-colors.svg?style=flat-square
