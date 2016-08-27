/**
 * Created by dharmendra on 25/8/16.
 */

productapp = angular.module('productapp');

productapp.controller('ProductController', ['$scope', function($scope) {
    $scope.save = function () {
        console.log('angular is working');
    };
  $scope.customer = {
    name: 'Naomi',
    address: '1600 Amphitheatre'
  };
}]);
