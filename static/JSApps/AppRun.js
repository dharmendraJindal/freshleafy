JSApps.run(["$rootScope", function ($rootScope) {

    //initialize empty cart
    $rootScope.cartItems = [];

    $rootScope.cartHandler = new CartItemHandler($rootScope);

}]);