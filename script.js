cookies = document.cookie.split('=');
cookies = cookies.filter((e, i) =>  i % 2 == 0) 
console.log(cookies.includes("test1"));
if (cookies.includes("test1") === true) {
	console.log("test1 is a cookie that exists");
}