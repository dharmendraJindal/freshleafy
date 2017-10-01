angular
  .module('MatApp', ['ngMaterial'])

  .controller('AppCtrl', function ($scope, $timeout, $mdSidenav, $log) {

  $scope.toggle = function() {
      $mdSidenav('left').toggle();
  };


  })
