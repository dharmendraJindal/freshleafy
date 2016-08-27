articlesapp.directive('fileModel', ['$parse', function ($parse) {
    return {
        restrict: 'A',
        link: function(scope, element, attrs) {
            var model = $parse(attrs.fileModel);
            var modelSetter = model.assign;

            element.bind('change', function(){
                scope.$apply(function(){
                    modelSetter(scope, element[0].files[0]);
                });
            });
        }
    };
}]);
//articlesapp.service('fileUpload', ['$http', function ($http) {
//    this.uploadFileToUrl = function(file, title, content, category, uploadUrl){
//        var fd = new FormData();
//        fd.append('featured_image', file);
//        fd.append('title', title);
//        fd.append('content', content);
//        fd.append('category', category);
//        console.log(fd);
//        $http.post(uploadUrl, fd, {
//            transformRequest: angular.identity,
//            headers: {'Content-Type': undefined}
//        })
//        .success(function(){
//        })
//        .error(function(){
//        });
//    }
//}]);

//
//<div class="form-group" >
//      <label>Image</label>
//        <input type="file" class="form-control"  file-model="featured_image"/>
//    </div>