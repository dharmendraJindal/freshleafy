/**
 * Created by dharmendra on 7/9/16.
 */

productapp.service("OrderSummaryService", ["$resource","$q","$http", function ($resource,$q,$http) {
    this.getOrderSummary=function(){
       var deferred=$q.defer();
       $http.get("/api/v1/product/ordersummary").then(function(data){
           deferred.resolve(data.data);
         }, function(status){
           deferred.reject(status);
       });

       return deferred.promise;
    };
}]);
