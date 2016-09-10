
productapp.controller("ProfileController", ["$location", "$scope", "Authentication", function ($location, $scope, Authentication) {
    var profile = {
        firstName: "",
        lastName: "",
        email: "",
        password: "",
        confirmPassword: "",
        phone_number: "",
        companyName: ""
    };
    $scope.profile = angular.copy(profile);
    $scope.updateProfile = updateProfile();
    viewProfile();


    function viewProfile() {
        Authentication.getProfile().then(function (profileAPIData) {
            loadProfileData(profileAPIData);
        }, function () {
        });
    }

    function loadProfileData(profileAPIData) {

        $scope.profile.firstName = profileAPIData.first_name ;
        $scope.profile.lastName = profileAPIData.last_name;
        $scope.profile.email = profileAPIData.email;
        $scope.profile.password = profileAPIData.password;
        $scope.profile.phone_number = profileAPIData.phonenumber;
        $scope.profile.companyName = profileAPIData.company

    }
    
    
    function updateProfile() {
        // if ($scope.ProfileForm.$invalid) {
        //     return false;
        // }
        Authentication.updateProfile($scope.profile).then(function () {
            $location.path('/home/profile');
        }, function () {
        });
    }
}]);
