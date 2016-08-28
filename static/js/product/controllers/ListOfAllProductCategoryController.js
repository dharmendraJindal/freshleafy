productapp.controller("ListOfAllProductCategoryController", ["$scope", "$routeParams", "$location",
    "Authentication", "ProductCategoryFactory",
    function ($scope, $rootScope, $location, Authentication, ProductCategoryFactory) {

        var product={
        name:'',
        price:'',
        category:'',
        grade:'',
        unit:'',
        quantity:1
        };

        $scope.productCategory = ProductCategoryFactory.query();
        
        $scope.productCategory.$promise.then(function (result) {
            $scope.categoryList = result;
            console.log(result);
        });

        $scope.products=[];

        for(var i=0;i<10;i++){
        var prod=angular.copy(product);
        prod.name="Potato";
        prod.price=10;
        prod.category="Vegetable";
        prod.grade=1;
        prod.unit="kg";

        $scope.products.push(prod);
        }

    }
]);