productapp.controller("ListOfAllProductCategoryController", ["$scope", "$routeParams", "$location",
    "Authentication", "ProductCategoryFactory",
    function ($scope, $rootScope, $location, Authentication, ProductCategoryFactory) {
        
        $scope.productCategory = ProductCategoryFactory.query();
        
        $scope.productCategory.$promise.then(function (result) {
            $scope.categoryList = result;
            console.log(result);
        });
    }
]);