// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract DocumentVerification {
    mapping(bytes32 => bool) public registeredDocuments;
    event DocumentRegistered(bytes32 hash);

    function registerDocument(bytes32 hash) public {
        require(!registeredDocuments[hash], "Document already exists!");
        registeredDocuments[hash] = true;
        emit DocumentRegistered(hash);
    }

    function verifyDocument(bytes32 hash) public view returns (bool) {
        return registeredDocuments[hash];
    }
}
