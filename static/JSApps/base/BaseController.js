JSApps.controller('BaseController', ["$scope","$mdSidenav","$location", function ($scope, $mdSidenav, $location) {

  $scope.toggleNav = function() {
      $mdSidenav('left').toggle();
  };

      $scope.cartCheckout = function () {
        $location.path('/cartcheckout');
    };

  }])