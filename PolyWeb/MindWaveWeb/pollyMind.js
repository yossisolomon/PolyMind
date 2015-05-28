var app = angular.module('pollyMind', []);

$scope.questionsArray={};

app.controller('questionController', function($scope, $http) {
	error(function(data, status, headers, config) {
	});
	$scope.questionText = "";
	angular.forEach(questions, function(question) 
	{
		
	};
});

app.controller('gotConnectedController', function($scope, $http) {
	$scope.connect="Connect";
	$http.get("localhost")
		.success(function(response) {
			$scope.questions = response.questions;
		});
	error(function(data, status, headers, config) {
	});

});