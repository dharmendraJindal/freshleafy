MatApp.controller('HomeController', function ($scope, $timeout, $mdSidenav, $log) {

  $scope.toggle = function() {
      $mdSidenav('left').toggle();
  };


  })