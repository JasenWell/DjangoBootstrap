
let flag = "../";

function getNow(s) {
    return s < 10 ? '0' + s: s;
}

function getCurrentTime() {
    const myDate = new Date();
    const year=myDate.getFullYear();        //获取当前年
    const month=myDate.getMonth()+1;   //获取当前月
    const date=myDate.getDate();            //获取当前日

    const h = myDate.getHours();              //获取当前小时数(0-23)
    const m=myDate.getMinutes();          //获取当前分钟数(0-59)
    const s=myDate.getSeconds();

    const now = year+'-'+getNow(month)+"-"+getNow(date)+" "+getNow(h)+':'+getNow(m)+":"+getNow(s);
    return now;
}
