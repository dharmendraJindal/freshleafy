productapp.controller("RegisterController", ["$location", "$scope", "Authentication",
    function ($location, $scope, Authentication) {
        $scope.account = {
            username: "",
            email: "",
            password: ""
        };
        $scope.register = register;

        function register() {
            Authentication.register($scope.account.username, $scope.account.email, $scope.account.password);
        }
    }]);