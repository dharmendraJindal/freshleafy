productapp.controller("ListOfAllProductCategoryController", ["$scope", "$routeParams", "$location",
    "Authentication", "ProductService",
    function ($scope, $rootScope, $location, Authentication, ProductService) {

        var product={
        name:'',
        price:'',
        category:'',
        grade:'',
        unit:'',
        quantity:1
        };

        $scope.products=[];

        var getProducts=function(){
          ProductService.getProducts().then(function(data){
          $.each(data,function(index,item){
             var prod=angular.copy(product);
             prod.name=item.name;
             prod.price=item.rate;
             prod.category="Vegetable";
             prod.grade=item.grade;
             prod.unit=item.unit;

             $scope.products.push(prod);
          });
          },function(){

          });
        };
        getProducts();

    }
]);