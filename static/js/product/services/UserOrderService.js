/**
 * Created by dharmendra on 7/9/16.
 */

productapp.service("UserOrderService", ["$resource","$q","$http", function ($resource,$q,$http) {
    this.getUserOrders=function(){
       var deferred=$q.defer();
       $http.get("/api/v1/product/userorder").then(function(data){
           deferred.resolve(data.data);
         }, function(status){
           deferred.reject(status);
       });

       return deferred.promise;
    };
}]);
