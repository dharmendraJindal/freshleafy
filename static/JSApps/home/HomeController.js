JSApps.controller('HomeController', ["$scope", "$timeout", "$mdSidenav", "$log", "$location", function ($scope, $timeout, $mdSidenav, $log, $location) {


    $scope.goToProductPage = function () {
        $location.path('/products');
    };


}])