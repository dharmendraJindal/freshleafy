JSApps.controller('HomeController', ["$scope", "$timeout", "$mdSidenav", "$log", "$location", function ($scope, $timeout, $mdSidenav, $log, $location) {

  $scope.toggle = function() {
      $mdSidenav('left').toggle();
  };

  $scope.goToProductPage = function () {
  $location.path('/products');
};


  }])