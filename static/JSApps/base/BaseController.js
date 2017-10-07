JSApps.controller('BaseController', ["$scope","$mdSidenav", function ($scope, $mdSidenav) {

  $scope.toggleNav = function() {
      $mdSidenav('left').toggle();
  };

  }])