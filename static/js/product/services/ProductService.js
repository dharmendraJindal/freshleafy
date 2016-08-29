productapp.service("ProductService", ["$resource","$q","$http", function ($resource,$q,$http) {
    this.getProducts=function(){
       var deferred=$q.defer();
       $http.get("/api/v1/product/products").then(function(data){
           deferred.resolve(data.data);
         }, function(status){
           deferred.reject(status);
       });

       return deferred.promise;
    };
}]);