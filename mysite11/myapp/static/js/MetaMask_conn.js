// MetaMask installation check
if (typeof web3 !== 'undefined') {
    console.log('MetaMask is installed');
    web3 = new Web3(web3.currentProvider);
    window.ethereum.enable();
}
else {
    console.log('MetaMask is not installed');
    var message = "메타마스크를 설치해주세요.";
    alert("크롬 브라우저를 통해 메타마스크를 설치해주세요.");
}

// Reading MetaMask accounts
web3.eth.getAccounts(function (err, accounts) {
    if (err != null) {
        console.log(err)
    }
    else if (accounts.length === 0) {
        console.log('MetaMask is locked');
        alert("메타마스크 계정에 로그인 해주세요.");
    }
    else {
        console.log('MetaMask is unlocked');
        console.log(accounts[0]);
    }

    // network check
    web3.version.getNetwork((err, netId) => {
        var network;
        switch (netId) {
            case "1":
                network = "Mainnet";
                break;
            case "3":
                network = "Ropsten";
                break;
            case "4":
                network = "Rinkeby";
                break;
            case "42":
                network = "Kovan";
                break;
            case '5777':
                network = "Ganache";
                break;
            default:
                network = "undefined";
                break;
        }

        // error raise 

        if (network == "undefined") {
            alert("MetaMask 연동 네트워크를 확인할 수 없습니다.");
        }
    });
    
    // detecting change of MetaMask accounts
    // not call back
    var accountInterval = setInterval(() => {
        web3.eth.getAccounts(function (err, accs) {
            if (accs != accounts[0]) {
                alert("MetaMask 로그인 계정이 변경되었습니다.");
                clearInterval(accountInterval);
                accounts[0] = accs;
                //location.href = "/";
            }
        });
    }, 2000); // accountInterval

}); // end of getAccounts Func
