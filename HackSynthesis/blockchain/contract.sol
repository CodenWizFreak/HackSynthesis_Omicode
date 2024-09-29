// SPDX-License-Identifier: MIT
pragma solidity ^0.8.27;

contract FundraisingCampaign {
    struct Contribution {
        uint amount;
        string location;
    }

    address public owner;
    mapping(address => Contribution[]) public contributions;
    uint public totalFunds;

    event ContributionMade(address indexed contributor, uint amount, string location);
    event FundsWithdrawn(address indexed owner, uint amount);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    constructor() {
        owner = msg.sender;
        totalFunds = 0;
    }

    function contribute(string memory location) public payable {
        require(msg.value > 0, "Contribution amount must be greater than zero");
        contributions[msg.sender].push(Contribution(msg.value, location));
        totalFunds += msg.value;
        emit ContributionMade(msg.sender, msg.value, location);
    }

    function getContributions(address contributor) public view returns (Contribution[] memory) {
        return contributions[contributor];
    }

    function withdraw() public onlyOwner {
        uint balance = address(this).balance;
        payable(owner).transfer(balance);
        emit FundsWithdrawn(owner, balance);
    }
}
