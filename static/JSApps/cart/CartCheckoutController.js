JSApps.controller("CartCheckoutController", ["$scope", "$rootScope", function ($scope, $rootScope) {

    $scope.products = $rootScope.cartItems;
    }
]);