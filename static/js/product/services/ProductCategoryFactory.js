
productapp.service("ProductCategoryService", ["$resource","$q","$http", function ($resource,$q,$http) {
    this.getProductCategories= function(){
       var deferred=$q.defer();
       $http.get("api/v1/product/categories").then(function(data){
           deferred.resolve(data.data);
         }, function(status){
           deferred.reject(status);
       });

       return deferred.promise;
    };
}]);
