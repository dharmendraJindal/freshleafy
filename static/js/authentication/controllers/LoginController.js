productapp.controller("LoginController", ["$location", "$scope", "Authentication",
    function ($location, $scope, Authentication) {
        $scope.account = {
            username: "",
            password: "",
            test : ""
        };
        $scope.login = login;
        activate();
        function activate() {
            if (Authentication.isAuthenticated()) {
                $location.url("/");
            }
        }

        function login() {
            if($scope.LoginForm.$invalid) {
            return false;
            }
            Authentication.login($scope.account.username, $scope.account.password);
        }
    }]);