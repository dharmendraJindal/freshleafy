productapp.controller('NavBarController', ["$scope", "Authentication",
    function ($scope, Authentication) {

        console.log("in controller");
        if (Authentication.isAuthenticated()) {
            $scope.UserLoggedIn = true;
        } else {
            $scope.UserLoggedIn = false;
        }

        $scope.logout = logout;
        function logout() {
            Authentication.logout();
        }
    }]);
