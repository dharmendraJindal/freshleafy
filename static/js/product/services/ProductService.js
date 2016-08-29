productapp.service("ProductService", ["$resource", function ($resource) {
    this.getProducts=function(){
       var deferred=$q.defer();
       $http.get("/api/v1/auth/register/").then(function(){
           deferred.resolve();
         }, function(){
           deferred.reject();
       });

       return deferred.promise;
    };
}]);