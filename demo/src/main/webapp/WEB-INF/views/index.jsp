<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="CACHE-CONTROL" content="NO-CACHE">
        <link rel="stylesheet" type="text/css" href="https:///cdnjs.cloudflare.com/ajax/libs/milligram/1.2.3/milligram.min.css">
        <title>Simple Storage Dapp test</title>
        <style>
            body {margin-left:50px;}
            #storedData {font-size:300%; margin-right:10px;}
            #newValue{width:200px; margin-right:10px;text-align:right;}
        </style>
    </head>
    <body>
        <h3>Simple Storage Dapp test</h3>
        <ul>
            <li>contract address: <span id="contractAddr"></span></li>
            <li>my account address: <span id="accountAddr"></span></li>
            <li>stored value: <span id="storedData"></span>
                <button onclick="getValue()">F5</button> (currnet block: <span id="lastBlock"></span>)</li>
            <li><input id="newValue" type="text"><button onclick="setValue()">store new value</button>
                <div id="result"></div></li>
            <li>After transaction is included into block, page will be updated automatically.</li>
        </ul>

        <!--contract address-->
        <!--script src="https://"></script>-->
    </body>
    <script src="D:\vscode\votingDapp\demo\bower_components\web3\dist\web3.js"></script>
<!-- script src="https://code.jquery.com/jquery-3.1.1.slim.min.js"></script -->
<script>
var contractAddress = '0x13a126ad46319e5e2881d94060c819e95604e6c7';
var abi = [{"constant":false,"inputs":[{"name":"x","type":"uint256"}],"name":"set","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"get","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"}];
var simpleStorageContract;
var simpleStorage;
window.addEventListener('load', function() {
  // Checking if Web3 has been injected by the browser (Mist/MetaMask)
  if (typeof web3 !== 'undefined') {
    // Use Mist/MetaMask's provider
    window.web3 = new Web3(web3.currentProvider);
  } else {
    console.log('No web3? You should consider trying MetaMask!')
    // fallback - use fallback strategy (local node / hosted node + in-dapp id mgmt / fail)
    window.web3 = new Web3(new Web3.providers.HttpProvider("http://localhost:7545"));
  }
  // start your app & access web3 freely:
  startApp();
});
function startApp() {
  simpleStorageContract = web3.eth.contract(abi);
  simpleStorage = simpleStorageContract.at(contractAddress);
  document.getElementById('contractAddr').innerHTML = getLink(contractAddress);
  web3.eth.getAccounts(function(e,r){
    document.getElementById('accountAddr').innerHTML = getLink(r[0]);
  });
  getValue();
}
function getLink(addr) {
  return '<a target="_blank" href=https://testnet.etherscan.io/address/' + addr + '>' + addr +'</a>';
}
function getValue() {
  simpleStorage.get(function(e,r){
    document.getElementById('storedData').innerHTML=r.toNumber();
  });
  web3.eth.getBlockNumber(function(e,r){
    document.getElementById('lastBlock').innerHTML = r;
  });
}
function setValue() {
  var newValue = document.getElementById('newValue').value;
  var txid
  simpleStorage.set(newValue, function(e,r){
    document.getElementById('result').innerHTML = 'Transaction id: ' + r + '<span id="pending" style="color:red;">(Pending)</span>';
    txid = r;
  });
  var filter = web3.eth.filter('latest');
  filter.watch(function(e, r) {
    getValue();
    web3.eth.getTransaction(txid, function(e,r){
      if (r != null && r.blockNumber > 0) {
        document.getElementById('pending').innerHTML = '(stroed block : ' + r.blockNumber + ')';
        document.getElementById('pending').style.cssText ='color:green;';
        document.getElementById('storedData').style.cssText ='color:green; font-size:300%;';
        filter.stopWatching();
      }
   });
 });
}
</script>
</html>