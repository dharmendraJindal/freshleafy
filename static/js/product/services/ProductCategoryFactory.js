productapp.factory("ProductCategoryFactory", ["$resource", function ($resource) {
    return $resource('api/v1/product/categories');
}]);